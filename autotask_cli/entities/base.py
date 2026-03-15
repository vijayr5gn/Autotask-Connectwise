from ..client import client

class BaseEntity:
    endpoint = ""
    display_fields = ["id"]
    required_fields = []

    # Capability flags — override to False for read-only entities
    can_create = True
    can_update = True
    can_delete = True

    # Child entity support — set parent_endpoint for entities that
    # are created/listed under a parent (e.g., CompanyNotes under Companies)
    parent_endpoint = None
    parent_id_field = None

    @classmethod
    def list(cls, limit=None, filters=None):
        if not filters:
            # Some entities don't have isActive; fall back to empty filter
            filters = [{"op": "gte", "field": "id", "value": 0}]

        all_items = []
        endpoint = f"{cls.endpoint}/query"

        max_per_page = 500
        if limit and limit < 500:
            max_per_page = limit

        body = {
            "filter": filters,
            "MaxRecords": max_per_page
        }

        data = client.request("POST", endpoint, json=body)
        items = data.get("items", [])
        all_items.extend(items)

        page_details = data.get("pageDetails", {})
        next_url = page_details.get("nextPageUrl")

        while next_url:
            if limit and len(all_items) >= limit:
                break

            data = client.request("POST", next_url, json=body)
            items = data.get("items", [])
            all_items.extend(items)

            page_details = data.get("pageDetails", {})
            next_url = page_details.get("nextPageUrl")

        if limit:
            return all_items[:limit]
        return all_items

    @classmethod
    def get(cls, entity_id):
        endpoint = f"{cls.endpoint}/{entity_id}"
        data = client.request("GET", endpoint)
        return data.get("item", {})

    @classmethod
    def create(cls, data):
        if not cls.can_create:
            raise PermissionError(f"{cls.__name__} does not support create operations.")

        # Handle child entities that require parent context
        if cls.parent_endpoint and cls.parent_id_field:
            parent_id = data.get(cls.parent_id_field)
            if parent_id:
                endpoint = f"{cls.parent_endpoint}/{parent_id}/{cls.endpoint}"
            else:
                endpoint = cls.endpoint
        else:
            endpoint = cls.endpoint

        return client.request("POST", endpoint, json=data)

    @classmethod
    def update(cls, entity_id, data):
        if not cls.can_update:
            raise PermissionError(f"{cls.__name__} does not support update operations.")

        # Handle child entities that require parent context
        if cls.parent_endpoint and cls.parent_id_field:
            parent_id = data.get(cls.parent_id_field)
            if parent_id:
                endpoint = f"{cls.parent_endpoint}/{parent_id}/{cls.endpoint}"
            else:
                endpoint = cls.endpoint
        else:
            endpoint = cls.endpoint

        data["id"] = entity_id
        return client.request("PATCH", endpoint, json=data)

    @classmethod
    def delete(cls, entity_id):
        if not cls.can_delete:
            raise PermissionError(f"{cls.__name__} does not support delete operations.")

        endpoint = f"{cls.endpoint}/{entity_id}"
        return client.request("DELETE", endpoint)
