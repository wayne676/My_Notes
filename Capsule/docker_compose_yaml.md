```yaml
development: &default
  adapter: postgresql
  database: dev_development

test: &test
  <<: *default
  database: test_test
```
& marks an alias for the node, for above example &default aliases the development node as "default"and the * references the aliased node with the name "default". The <<: inserts the content of that node.

就是把 development 起个别名然后放在 test 下面 database 之前