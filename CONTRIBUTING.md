# How to contribute to awesome-openaccess

We accept contributions from anyone. The criteria is that the contribution must refer to a project that has published their data as OpenAccess in one way or another. This typically looks like museum or other cultural org metadata and/or images placed somewhere online, with some kind of accompanying license regarding use of that data.

To contribute, please follow the steps below. If your data is from an organization other than a museum, please indicate the type of organization in the `type` field.

**Note:** Please do NOT regenerate the `README.md` file by using the python script in the `bin` folder. We will do this once we accept your pull request.

## On GitHub

### 1. Create a new file in the [data folder](/data) named as follows:

- `org-name.yml`.

### 2. create your file following this example

```
---
name: Auckland Museum 
type: Museum
location: Auckland, New Zealand
data: [csv, json, api]
url: https://api.aucklandmuseum.com/
github: https://github.com/AucklandMuseum/Collection-Data
```

### 3. Submit a pull request.

We will review your pull request, merge it in if accepted and regenerate the `README.md` file for you. 
