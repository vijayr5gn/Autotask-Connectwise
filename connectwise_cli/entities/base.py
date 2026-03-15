from ..client import client

class BaseEntity:
    endpoint = ""
    display_fields = ["id"]
    required_fields = []
    can_create = True
    can_update = True
    can_delete = True
    parent_endpoint = None   # e.g. "company/companies"
    parent_id_field = None   # e.g. "parentId"

    @classmethod
    def list(cls, limit=None, filters=None):
        all_items = []
        page = 1
        page_size = 1000
        
        while True:
            params = {
                "pageSize": page_size,
                "page": page
            }
            if filters:
                 params["conditions"] = filters
            
            data = client.request("GET", cls.endpoint, params=params)
            if not data or not isinstance(data, list):
                break
            
            all_items.extend(data)
            
            # If we got fewer than page_size, it's the last page
            if len(data) < page_size:
                break
                
            if limit and len(all_items) >= limit:
                break
                
            page += 1
            
        if limit:
            return all_items[:limit]
        return all_items

    @classmethod
    def get(cls, entity_id):
        endpoint = f"{cls.endpoint}/{entity_id}"
        return client.request("GET", endpoint)

    @classmethod
    def create(cls, data):
        endpoint = f"{cls.endpoint}"
        return client.request("POST", endpoint, json=data)

    @classmethod
    def update(cls, entity_id, data):
        endpoint = f"{cls.endpoint}/{entity_id}"
        return client.request("PATCH", endpoint, json=data)

    @classmethod
    def delete(cls, entity_id):
        endpoint = f"{cls.endpoint}/{entity_id}"
        return client.request("DELETE", endpoint)
