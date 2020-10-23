import json

managers = {}
watchers = {}

with open('source_file_2.json') as f:
  data = json.load(f)


for project in data:
  projectName = project["name"] 

  for managerName in project["managers"]:
    if not managerName in managers:
      managers[managerName] = []
    projPrior = {
      "name": projectName,
      "priority": project["priority"]
    }
    managers[managerName].append(projPrior)

  for watcherName in project["watchers"]:
    if not watcherName in watchers:
      watchers[watcherName] = []
    projPrior = {
      "name": projectName,
      "priority": project["priority"]
    }
    watchers[watcherName].append(projPrior)

for mName in managers:
  managerProjects = managers[mName]
  managers[mName] = sorted(managerProjects, key=lambda k: k['priority'])
  newlist = []
  for m in managers[mName]:
    newlist.append(m["name"])
  managers[mName] = newlist

for wName in watchers:
  watcherProjects = watchers[wName]
  watchers[wName] = sorted(watcherProjects, key=lambda k: k['priority'])
  newlist = []
  for w in watchers[wName]:
    newlist.append(w["name"])
  watchers[wName] = newlist

with open('managers.json', 'w') as mjf:
  json.dump(managers, mjf)

with open('watchers.json', 'w') as wjf:
  json.dump(watchers, wjf)