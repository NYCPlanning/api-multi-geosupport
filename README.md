# api-multi-geosupport

This project will use docker compoase to create a multi container geosupport api that allows users to make queries against different versions of geosupport

```
docker run -itd \
    -p 5001:5001 \
    -v `pwd`:/home/app \
    -w /home/app \
    continuumio/miniconda3:4.6.14 bash -c "pip install -r requirements.txt; python app.py"
```