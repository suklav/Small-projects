# Read items from a list. Accounting for all data types if possible
def append_lists(email): 
    if '@' in email:
        email_slicer = email.split('@')
        user_name.append(email_slicer[0])
        domain_name.append(email_slicer[1])
    if '[at]' in email:
        email_slicer = email.split('[at]')
        user_name.append(email_slicer[0])
        domain_name.append(email_slicer[1])
    
        
    return user_name, domain_name

if __name__ == '__main__':
    # Delcare variables
    email_list = ['debapriyo-[AT]-isical-[DOT]-ac-[DOT]-in', 2, 3.14, 'smcssg2624@iacs.res.in', 'pq1','suklav.cs [at] gmail [DOT] com', True]
    user_name = []
    domain_name = []
    
    # Loop through the list and apply function
    for email in email_list:
        try:
            append_lists(email)
        except TypeError:
            continue
    domain_name1 = [item.replace(" [dot] ", ".").replace(" [DOT] ", ".") for item in domain_name]
    print(f'Usernames: {user_name} \nDomains: {domain_name1}')
