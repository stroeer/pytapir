FROM public.ecr.aws/lambda/python:3.12

ADD ../../requirements.txt .
COPY ../../stroeer stroeer/

RUN dnf -y install zip gcc gcc-c++ && dnf -y clean all  && rm -rf /var/cache
RUN pip install --requirement requirements.txt --target python
RUN cp -R stroeer python/
RUN zip --recurse-paths --verbose layer.zip python