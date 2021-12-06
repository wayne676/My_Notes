docker file - build image
```
From xxx as newxxx
WORKDIR path/to/workdir
COPY 
RUN java etc
FROM xxx as nnewxxx
ARG if neceessary
LABEL equivalent to add nick name
USER if necessary
ENV 
WORKDIR
COPY --from=newxx path/to/workdir(old) ./(new)
COPY path/file(folder) newpath/file(folder)

ENTRYPOINT ["command","para1","para2"]
```


docker compose - config ports, dependency relationship, healthcheck, env virable

helm chars deploy the k8s