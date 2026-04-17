valid_domains = {"gmail.com", "yahoo.com", "outlook.com"}
registered_emails = set()


def validate_email(email):
    email = email.lower().strip()
    if "@" not in email:
        return False, "Invalid Format"
    
    user, domain = email.split("@")
    
    if domain not in valid_domains:
        return False, "Invalid Domain"
    
    if email in registered_emails:
        return False, "Already Registered"
    
    return True, "Valid"


def register_email(email):
    is_valid, message = validate_email(email)
    
    if is_valid:
        registered_emails.add(email)
        return "Success"
    else:
        return message


def find_by_domain(domain):
    return {email for email in registered_emails if email.endswith(domain)}


# Testing
emails_to_test = ["ali@gmail.com", "sara@xeven.ai", "ali@gmail.com", "hack@outlook.com"]

for e in emails_to_test:
    result = register_email(e)
    print(f"Email: {e:<20} Result: {result}")

print("\nRegistered Emails:", registered_emails)
print("\nGmail Users:", find_by_domain("gmail.com"))