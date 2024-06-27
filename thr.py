cellName = "AZWAPUAUWAISA04Cell01"

node1Name = "AZWAPUAUWAISA04Node01"

node2Name = "AZWAPUAUWAISA05Node01"

server1Name = "AISStage01"

server2Name = "AISStage02"

serverType = "APPSERVER"

dmgrName = "dmgr"

javaAgentArg1 = "-javaagent:/tech/newrelic/newrelic.jar"

javaAgentArg2 = "-Dnewrelic.environment=AIS_STG"

genericJvmArgs = javaAgentArg1 + " " + javaAgentArg2

 

 

 

#### SET MAX LOG FILE SIZE TO 100MB

s1 = AdminConfig.getid('/Cell:' + cellName + '/Node:' + node1Name + '/Server:' + server1Name + '/')

stdoutlog1 = AdminConfig.showAttribute(s1, 'outputStreamRedirect')

stderrlog1 = AdminConfig.showAttribute(s1, 'errorStreamRedirect')

 

AdminConfig.modify(stdoutlog1, [['rolloverSize', 100]])

AdminConfig.modify(stderrlog1, [['rolloverSize', 100]])

 

 

 

s2 = AdminConfig.getid('/Cell:' + cellName + '/Node:' + node2Name + '/Server:' + server2Name + '/')

stdoutlog2 = AdminConfig.showAttribute(s2, 'outputStreamRedirect')

stderrlog2 = AdminConfig.showAttribute(s2, 'errorStreamRedirect')

 

AdminConfig.modify(stdoutlog2, [['rolloverSize', 100]])

AdminConfig.modify(stderrlog2, [['rolloverSize', 100]])

 

AdminConfig.save()

 

 

#### ENABLE APPLICATION SECURITY

 

# Set application security

AdminTask.setAdminActiveSecuritySettings('[-appSecurityEnabled true]')

 

 

#### ENABLE AUTOMATIC REPOSITORY CHECKPOINT

AdminTask.setAutoCheckpointEnabled('[-autoCheckpointEnabled true]')

 

 

#### ADD NEWRELIC JAVA ARGUMENTS

 

AdminTask.setGenericJVMArguments('[-serverName ' + server1Name + ' -nodeName ' + node1Name + ' -genericJvmArguments "' + genericJvmArgs + '"]')

 

 

AdminConfig.save()

 

# Synchronize all nodes

syncResult = AdminControl.completeObjectName('type=NodeSync,node=*,*')

print "Node synchronization result: " + syncResult

 
