##  Ex. 1 HTTP Status I
Select the HTTP code for the next errors
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

    Note: ignore 1xx and WebDav 

* I cannot access that web if I'm not logged:
  * **401 Not authorized** 

* I'm logged but I cannot access that page
  * **403 Forbidden**

* That was deleted
  * **410 Gone** or 404 Not found

* I started uploading, but I have to check another link to see if it is there
  * **200 OK** or 202 Accepted
    * Redirections 3xx are not good because you end up downloading the file

* That query parameter is wrong
  * **400 Bad Request**
    * 406 Not Acceptable is usually focused in protocols 
    * 409 Conflict and 422 unprocessable entity are becoming more usual
    * But a query parameter error is usually a 400. 422 and others usually point to a problem with
      the body, and 409 with the current status of the accessed resource

* There are no resources with that ID
  * **404 not found**
  * if is a GET on a collection, could be 200 with no result

* My request was good, but it will take time to resolve
  * **202 Accepted**

* The resource was deleted but no extra info was provided
  * **204 No Content**

* Added a product to the collection
  * **201 Created**

Got the info I needed
  * **200 OK**

### Common errors:

- Using 1xx, 3xx and 5xx, and some WebDav exclusive codes
  - There wasn't any statement suggesting Server Side error (5xx)
  - Some redirections could have made sense
- some 2xx caused confusion, mostly related to a too broad statement


## Ex.2  HTTP Status II

Select the right HTTP verb

* Added some info to my profile
  * PUT/PATCH
 
* Checked my profile as it is now
  * GET

* Created a new product
  * POST

* Created several new products
  * POST 

* Removed one product
  * DELETE 

* Replaced a product
  * PUT 

* Want to know if the image is there, without downloading 
  * HEAD  
