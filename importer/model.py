#!/usr/bin/env python
import unicodedata
import string
import copy

class DataEntry(object):
    def __init__(self, *a, **kw):
        self.description = kw.get('description')
        self.contact_name = kw.get('contactName')
        self.keywords = kw.get('keywords')
        self.access_level = kw.get('accessLevel')
        self.publisher = kw.get('publisher')
        self.landing_page = kw.get('landingPage')
        self.license = kw.get('license')
        self.title = kw.get('title')
        self.temporal = kw.get('temporal')
        self.mbox = kw.get('mbox')
        self.version = kw.get('version')
        self.distribution = []
        for d in kw.get('distribution', []):
            self.distribution.append(DataDistribution(d))

class DataDistribution(object):
    def __init__(self, d):
        self.accessURL = d.get('accessURL')
        self.format = d.get('format')

class CkanDataset(object):

    license_dict = {
        'https://creativecommons.org/licenses/by/4.0/legalcode' : 'cc-by'
    }

    def __init__(self, entry, modalidad):
        self.notes = unicode(entry.description)
        self.title = unicode(entry.title)
        self.name = unicode('-'.join(remove_accents(entry.title).lower().split()))
        self.tags = [{'name': unicode(k)} for k in entry.keywords] + [{'name': unicode(modalidad)}]
        self.author = unicode(entry.contact_name)
        self.author_email = unicode(entry.mbox)
        self.maintainer = unicode(entry.contact_name)
        self.maintainer_email = unicode(entry.mbox)
        self.version = entry.version
        if entry.temporal:
            self.valid_from = entry.temporal.split('/')[0]
            self.valid_until = entry.temporal.split('/')[1]
        self.license = self.license_dict.get(entry.license)
        self.owner_org = unicode('-'.join(remove_accents(entry.publisher).lower().split()))
        self.resources = []
        for d in entry.distribution:
            self.resources.append(CkanResource(d, self.title))
        self.modalidad = u'recolecta'
        self.private = True

    def as_dict(self):
        d = self.__dict__.copy()
        d['resources'] = [r.__dict__ for r in self.resources]
        #print d['resources']
        return d

    def __str__(self):
        d = self.as_dict()
        c = 1
        rep = 'Dataset: %s\n\n' % self.title
        for k in d:
            if k == 'resources':
                res = d[k]
                for r in res:
                    rep += 'Recurso Nro. %s\n' % str(c)
                    for i in r:
                        rep += i + ': ' + unicode(r[i]) + '\n'
                    c += 1
            elif k == 'tags':
                tags = ''
                for t in d[k]:
                    tags += t['name'] + ', '
                tags = tags[0:-2]
                rep += 'tags' + ': ' + tags + '\n'
            else:    
                rep += k + ': ' + unicode(d[k]) + '\n'
        return rep




class CkanResource(object):
    def __init__(self, distribution, title):
        self.name = title + ' ' + distribution.format.upper()
        self.format = distribution.format
        self.url = unicode(distribution.accessURL)


def remove_accents(data):
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.ascii_letters + ' ').lower()
