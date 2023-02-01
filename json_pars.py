import json 

def kuber_event_pars(json_output):
    data = json_output
    for keys in data.keys():
        if keys == "metadata":
            name = data["metadata"]["name"] 
            namespace = data["metadata"]["namespace"]
        final_message = f"""name = {name}\nnamespace = {namespace}\nreason = {data["reason"]}\nmessage = {data["message"]}\nsomeObject = {data["involvedObject"]["kind"]} , {data["involvedObject"]["uid"]}\neventTime = {data["eventTime"]}\n
    """
    print(final_message)
    return final_message


