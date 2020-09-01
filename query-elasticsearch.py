from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.search(index="dataset_record", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("dataset_name=%(dataset_name)s, dataset_description=%(dataset_description)s, "
          "dataset_owner=%(dataset_owner)s, dataset_tags=%(dataset_tags)s" % hit["_source"])
