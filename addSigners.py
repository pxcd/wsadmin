cellName = "AZWAPUAUWAISA04Cell01"

node1name = "AZWAPUAUWAISA04Node01"

node2name = "AZWAPUAUWAISA05Node01"

 

# add the 3 signer certs to CellDefaultTrustStore

AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):' + cellName + ' -certificateFilePath d:/tech/certs/aaa.cer -base64Encoded true -certificateAlias aaa ]')

AdminTask.getSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):' + cellName + ' -certificateAlias aaa ]')

AdminTask.listSignerCertificates('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):' + cellName + ' ]')

 

 

AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):' + cellName + ' -certificateFilePath d:/tech/certs/usertrust.cer -base64Encoded true -certificateAlias usertrust ]')

AdminTask.getSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):' + cellName + ' -certificateAlias usertrust ]')

AdminTask.listSignerCertificates('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):' + cellName + ' ]')

 

AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):' + cellName + ' -certificateFilePath d:/tech/certs/sectigo.cer -base64Encoded true -certificateAlias sectigo]')

AdminTask.getSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):' + cellName + ' -certificateAlias usertrust ]')

AdminTask.listSignerCertificates('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):' + cellName + ' ]')

 

 

# add the 3 signer certs to first node

AdminTask.addSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node1name + '  -certificateFilePath d:/tech/certs/aaa.cer -base64Encoded true -certificateAlias aaa ]')

AdminTask.getSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node1name + '  -certificateAlias aaa ]')

AdminTask.listSignerCertificates('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node1name + '  ]')

 

AdminTask.addSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node1name + '  -certificateFilePath d:/tech/certs/sectigo.cer -base64Encoded true -certificateAlias sectigo]')

AdminTask.getSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node1name + '  -certificateAlias aaa ]')

AdminTask.listSignerCertificates('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node1name + '  ]')

 

AdminTask.addSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node1name + '  -certificateFilePath d:/tech/certs/usertrust.cer -base64Encoded true -certificateAlias usertrust ]')

AdminTask.getSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node1name + '  -certificateAlias aaa ]')

AdminTask.listSignerCertificates('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node1name + '  ]')

 

 

# add the 3 signer certs to second node (optional)

AdminTask.addSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node2name + '  -certificateFilePath d:/tech/certs/aaa.cer -base64Encoded true -certificateAlias aaa ]')

AdminTask.getSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node2name + '  -certificateAlias aaa ]')

AdminTask.listSignerCertificates('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node2name + '  ]')

 

AdminTask.addSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node2name + '  -certificateFilePath d:/tech/certs/sectigo.cer -base64Encoded true -certificateAlias sectigo]')

AdminTask.getSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node2name + '  -certificateAlias aaa ]')

AdminTask.listSignerCertificates('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node2name + '  ]')

 

AdminTask.addSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node2name + '  -certificateFilePath d:/tech/certs/usertrust.cer -base64Encoded true -certificateAlias usertrust ]')

AdminTask.getSignerCertificate('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node2name + '  -certificateAlias aaa ]')

AdminTask.listSignerCertificates('[-keyStoreName NodeDefaultTrustStore -keyStoreScope (cell):' + cellName + ':(node):' + node2name + '  ]')

 

 

 

 

# Save the configuration changes

AdminConfig.save()

 

# Synchronize all nodes

syncResult = AdminControl.completeObjectName('type=NodeSync,node=*,*')

print "Node synchronization result: " + syncResult

 