from benedict import benedict

raw_data = {
  "user": {
    "profile": {
      "contact": {
        "email": "user@example.com",
        "phone": "+123456789"
      },
      "settings": {
        "theme": "dark",
        "notifications": True
      }
    }
  }
}

d1 = benedict(raw_data)
json_str = '{"user": {"profile": {"contact": {"email": "test@example.com"}}}}'
d2 = benedict.from_json(json_str)
email1 = d1["user.profile.contact.email"]
email2 = d2["user.profile.contact.email"]
print(email1)
print(email2)
phone = d1.get("user.profile.contact.phone", "+000000000")
phone = d2.get("user.profile.contact.phone")
print(phone)
