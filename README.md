# api-multi-geosupport

This project will use docker compoase to create a multi container geosupport api that allows users to make queries against different versions of geosupport

### Instructions:
1.  make sure you have docker compose installed
```
docker-compose up
```
2.  to see if it's working, try: 
```
curl 0.0.0.0:5000/19b2/geocode/1b?house_number=120&street_name=broadway&borough=MN

curl 0.0.0.0:5000/19b/geocode/1b?house_number=120&street_name=broadway&borough=MN
```

3. __Note:__ currently only 19[a, b, b2], 18[a, b, c, d] are implemented, feel free to add more ...