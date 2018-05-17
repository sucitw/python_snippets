# NiFi Scripting Samples
This space contains python script exsamples for using in Apache NiFi's scripting components, especially the ExecuteScript processor.


## ExecuteScript Samples
| Script             | Description                                       |
| :----------------- | :------------------------------------------------ |
| update_attribute.py | Read flowfile and update flowfile's attributes |
| read_update_content.py| Read and overwirte content |
| json_transform.py  | Update content of json format flowfile                       |



 


## Variable used in ExecuteScript
 | Variable Name | Description          |
 | :------------ | :------------------- |
 | session       | ProcessSession       |
 | context       | ProcessContext       |
 | log           | Log Component        |
 | REL_SUCCESS   | Success Relationship |
 | REL_FAILURE   | Failure Relationship |

## Reference:
* [BatchIQ](https://github.com/BatchIQ/nifi-scripting-samples)
* [ExecuteScript Cookbook](https://community.hortonworks.com/articles/75032/executescript-cookbook-part-1.html)