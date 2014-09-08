#!/usr/bin/env python
# encoding: utf-8
"""
microdata.py

Created by Alex Stolz on 2012-10-05.
Copyright (c) 2012 Universität der Bundeswehr München. All rights reserved.
"""
from rdflib.term import BNode, Literal, URIRef
from rdflib.exceptions import Error
from rdflib.serializer import Serializer
from rdflib.namespace import Namespace, RDF, RDFS
from rdflib.collection import Collection
from rdflib.util import first, more_than

__all__ = ['MicrodataSerializer', 'MicrodataVisibleSerializer']


OWL_NS = Namespace('http://www.w3.org/2002/07/owl#')
indent_string = "  "

class MicrodataSerializer(Serializer):
    
    def __init__(self, store, max_depth=3):
        super(MicrodataSerializer, self).__init__(store)
        #self.namespaces = {}
        #self._ns_rewrite = {}
        
    def relativize(self, uri, base=None):
        if not base:
            base = self.base
        if base is not None and uri.startswith(base):
            uri = URIRef(uri.replace(base, "", 1))
        return uri
    
    def extract_base(self, uri):
        if "#" in uri:
            return uri.rsplit("#", 1)[0]+"#"
        elif "/" in uri:
            return uri.rsplit("/", 1)[0]+"/"
        else:
            return None

    """
    def addNamespace(self, prefix, namespace):
        # Turtle does not support prefix that start with _ 
        # if they occur in the graph, rewrite to p_blah
        # this is more complicated since we need to make sure p_blah
        # does not already exist. And we register namespaces as we go, i.e.
        # we may first see a triple with prefix _9 - rewrite it to p_9
        # and then later find a triple with a "real" p_9 prefix 

        # so we need to keep track of ns rewrites we made so far.

        if (prefix > '' and prefix[0] == '_') \
              or self.namespaces.get(prefix, namespace) != namespace:

            if prefix not in self._ns_rewrite:
                p="p"+prefix
                while p in self.namespaces:
                    p="p"+p
                self._ns_rewrite[prefix]=p

        prefix=self._ns_rewrite.get(prefix,prefix)
        return prefix

    def getQName(self, uri, gen_prefix=True):
        if not isinstance(uri, URIRef):
            return None

        parts=None
        
        try: 
            parts = self.store.compute_qname(uri, generate=gen_prefix)
        except: 

            # is the uri a namespace in itself?
            pfx = self.store.store.prefix(uri)
        
            if pfx is not None:
                parts = (pfx, uri, '')
            else: 
                # nothing worked
                return None

        prefix, namespace, local = parts
        # Local parts with '.' will mess up serialization
        if '.' in local:
            return None
        prefix=self.addNamespace(prefix, namespace)

        return u'%s:%s' % (prefix, local)
    """

    def serialize(self, stream, base=None, encoding=None, **args):
        self.__serialized = {}
        self.base = base
        store = self.store
        self.__stream = stream
        encoding = self.encoding
        self.write = write = lambda uni: stream.write(uni.encode(encoding, 'replace'))
        
        self.max_depth = args.get("max_depth", 3)
        assert self.max_depth>0, "max_depth must be greater than 0"
        
        #namespaces = {}
        #self.nm = nm = store.namespace_manager
        
        #possible = set(set(
        #store.predicates()).union(store.objects(None, RDF.type))).union([o.datatype for o in store.objects() if isinstance(o, Literal) and o.datatype])
              
        #namespaces["rdf"] = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        #for predicate in possible:
        #    prefix, namespace, local = nm.compute_qname(predicate)
        #    namespaces[prefix] = namespace
            
        #write("<div xmlns=\"http://www.w3.org/1999/xhtml\"")
        #for prefix in namespaces:
        #    write("\n  xmlns:%s=\"%s\"" % (prefix, namespaces[prefix]))
        #write(">")
        write("<div>")
        
        # Write out subjects that can not be inline
        for subject in store.subjects():
            if (None, None, subject) in store:
                if (subject, None, subject) in store:
                    self.subject(subject, 1)
            else:
                self.subject(subject, 1)
        
        # write out anything that has not yet been reached
        # write out BNodes last (to ensure they can be inlined where possible)
        bnodes = set()
        for subject in store.subjects():
            if isinstance(subject, BNode):
                bnodes.add(subject)
                continue
            self.subject(subject, 1)
            
        #now serialize only those BNodes that have not been serialized yet
        for bnode in bnodes:
            if bnode not in self.__serialized:
                self.subject(subject, 1)
            
        write("\n</div>")
        self.__serialized = None


    def subject(self, subject, depth=1, skip_node=False):
        store = self.store
        write = self.write
        indent = "\n"+indent_string*depth
        if skip_node:
            depth = depth-1
        
        if not subject in self.__serialized:
            self.__serialized[subject] = 1
            type = first(store.objects(subject, RDF.type))
            
            #try:
            #    self.nm.qname(type)
            #except:
            #    type = None

            element = type or RDFS.Resource

            if not skip_node:
                if isinstance(subject, BNode):# not referenced more than once
                    if more_than(store.triples((None, None, subject)), 1):
                        write("%s<div itemtype=\"%s\" itemid=\"%s\" itemscope>" % (indent, element, fix(subject)))
                    else:
                        write("%s<div itemtype=\"%s\" itemscope>" % (indent, element))
                else:
                    write("%s<div itemtype=\"%s\" itemid=\"%s\" itemscope>" % (indent, element, self.relativize(subject)))
            
            context = self.extract_base(element)
            
            if (subject, None, None) in store:
                for predicate, object in store.predicate_objects(subject):
                    if not (predicate == RDF.type and object == type):
                        self.predicate(predicate, object, depth+1, context)
            
            if not skip_node:
                write("%s</div>" % indent)
        
    def predicate(self, predicate, object, depth=1, context=None):
        store = self.store
        write = self.write
        indent = "\n"+indent_string*depth

        if isinstance(object, Literal):
            write("%s<meta itemprop=\"%s\"" % (indent, self.relativize(predicate, context)))
            #if object.language:
            #    write(" xml:lang=\"%s\"" % object.language)
            #elif object.datatype:
            #    write(" datatype=\"%s\"" % self.getQName(object.datatype))
            write(" content=\"%s\" />" % object)
        elif object in self.__serialized or not (object, None, None) in store:
            write("%s<link itemprop=\"%s\"" % (indent, self.relativize(predicate, context)))
            if isinstance(object, BNode) and more_than(store.triples((None, None, object)), 0):
                write(" href=\"%s\" />" % fix(object))
            else:
                write(" href=\"%s\" />" % self.relativize(object))
        else:
            if first(store.objects(object, RDF.first)): # may not have type RDF.List
                self.__serialized[object] = 1
                
                # Warn that any assertions on object other than
                # RDF.first and RDF.rest are ignored... including RDF.List
                import warnings
                warnings.warn(
                    "Assertions on %s other than RDF.first " % repr(object) + \
                    "and RDF.rest are ignored ... including RDF.List", 
                    UserWarning, stacklevel=2)
                
                col = Collection(store, object)
                for item in col:
                    if isinstance(item, BNode):
                        write("%s<link itemprop=\"%s\" href=\"%s\" />" % (indent, self.relativize(predicate, context), fix(item)))
                    elif isinstance(item, URIRef):
                        write("%s<link itemprop=\"%s\" href=\"%s\" />" % (indent, self.relativize(predicate, context), self.relativize(item)))
                    else:
                        write("%s<link itemprop=\"%s\" href=\"%s\" />" % (indent, self.relativize(predicate, context), item))
                    if not isinstance(item, URIRef):
                        self.__serialized[item] = 1
            else:
                if first(store.triples_choices((object, 
                                                RDF.type, 
                                                [OWL_NS.Class,RDFS.Class]))) \
                      and isinstance(object, URIRef):
                    write("%s<link itemprop=\"%s\" href=\"%s\" />" % (indent, self.relativize(predicate, context), self.relativize(object)))
                    
                elif depth <= self.max_depth:
                    write("%s<div itemprop=\"%s\"" % (indent, self.relativize(predicate, context)))
                    if first(store.objects(object, RDF.type)):
                        write(" itemtype=\"%s\"" % first(store.objects(object, RDF.type)))
                    if isinstance(object, URIRef):
                        write(" itemid=\"%s\"" % object)
                    write(" itemscope>")
                    self.subject(object, depth+1, True) # skip node
                    write("%s</div>" % indent)
                
                elif isinstance(object, BNode):
                    if not object in self.__serialized \
                    and (object, None, None) in store \
                    and len(list(store.subjects(object=object))) == 1:
                        #inline blank nodes if they haven't been serialized yet and are
                        #only referenced once (regardless of depth)
                        #write(">")
                        self.subject(object, depth+1)
                        #write(indent)
                    else:
                        write("%s<link itemprop=\"%s\" href=\"%s\" />" % (indent, self.relativize(predicate, context), fix(object)))
                    
                else:
                    write("%s<link itemprop=\"%s\" href=\"%s\" />" % (indent, self.relativize(predicate, context), self.relativize(object)))
                
                
# TODO:
def fix(val):
    "strip off _: from nodeIDs... as they are not valid NCNames"
    if val.startswith("_:"):
        return val[2:]
    else:
        return val

