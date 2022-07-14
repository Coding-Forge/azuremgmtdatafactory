
class Print_Helper:

    def __init__(self):
        self.name=None

    def print_item(self, group):
        """Print an Azure object instance."""
        print("\tName: {}".format(group.name))
        print("\tId: {}".format(group.id))
        if hasattr(group, 'location'):
            print("\tLocation: {}".format(group.location))
        if hasattr(group, 'tags'):
            print("\tTags: {}".format(group.tags))
        if hasattr(group, 'properties'):
            self.print_properties(group.properties)

    def print_properties(self, props):
        """Print a ResourceGroup properties instance."""
        if props and hasattr(props, 'provisioning_state') and props.provisioning_state:
            print("\tProperties:")
            print("\t\tProvisioning State: {}".format(props.provisioning_state))
        print("\n\n")


    def print_activity_run_details(self, activity_run):
        """Print activity run details."""
        print("\n\tActivity run details\n")
        print("\tActivity run status: {}".format(activity_run.status))
        if activity_run.status == 'Succeeded':
            print("\tNumber of bytes read: {}".format(activity_run.output['dataRead']))
            print("\tNumber of bytes written: {}".format(activity_run.output['dataWritten']))
            print("\tCopy duration: {}".format(activity_run.output['copyDuration']))
        else:
            print("\tErrors: {}".format(activity_run.error['message']))



def is_empty(a):
    return not a

def get_all_keys(d):
    for key, value in d.items():
        yield key
        if isinstance(value, dict):
            yield from get_all_keys(value)


def look_in_string(search_string, search_value, end_value)->list:
    '''
    search_string is the string that you want to search on \n
    search_value is the character or string of characters to find \n
    end_value is the character that you want to find

    returns a list

    The function is used for finding a block of text using the search_value \n
    as the starting point and the end_value as the ending point. This allows\n
    a user to replace all of that range with another set of text
    '''
    i=0
    search_pairs = []
    while i < len(search_string):
        start = i
        end = len(search_string)
        try:
            start = search_string.index(search_value,start,end)
            carry = search_string.index(end_value,start+1,end)
            found_value = search_string[start:carry]
            search_pairs.append(found_value)
            i += start

        except:
            print('==================>>>>>>>>>i guess i threw an error<<<<<<<==================')
            i = len(search_string)

    return search_pairs