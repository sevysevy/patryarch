




def json_tree(list):

	arcdict = {}
	node4 = []
	divdict = {}
	node3 = []
	sseriedict = {}
	node2 = []
	seriedict = {}
	json = []
	dicsv = {"text":'le repertoire est vide'}
	

	try:
		for serie in list:
			node2 = []
			try:
				for sousserie in serie["nodes"]:
					node3 = []
					try:
						for division in sousserie["nodes"]:
							node4 = []
							try:
								for archives in division["nodes"]:
									link = 'archive/' + str (archives["id"]) +'/detail/'
									arcdict = {"text":archives["text"] , "href": link  ,"tags": [archives["nbrSousDoc"]],"tag":archives["tag"],"id":archives["id"]}
									node4.append(arcdict)
							except:
								dicav = {"text":'vide'}
								node4.append(dicav)

							link = 'division/' + str(division["id"]) + '/detail/'
							divdict = {"text":division["text"] ,"href":link ,"nodes": node4,"id":division["id"],"tag":division["tag"]}
							node3.append(divdict)
					except:
						dicdv = {"text":'vide'}
						node3.append(dicdv)

					link = 'sousserie/' + str(sousserie["id"]) + '/detail/'  
					sseriedict = {"text":sousserie["text"] ,"href":link, "nodes": node3,"id":sousserie["id"],"tag":sousserie["tag"]}
					node2.append(sseriedict)

			except:
				dicssv = {"text":'vide'}
				node2.append(dicssv)

			link = 'serie/' + str (serie["id"]) +'/detail/'
			seriedict = {"text" : serie["text"] , "href": link  , "nodes":node2,"id":serie["id"],"tag":serie["tag"]}
			json.append(seriedict)

	except:
		#json.append(dicsv)
		pass
		

	return (json)


def json_treew(list):

	arcdict = {}
	node4 = []
	divdict = {}
	node3 = []
	sseriedict = {}
	node2 = []
	seriedict = {}
	json = []
	dicsv = {"title":'le repertoire est vide'}
	
	try:
		for serie in list:
			node2 = []
			try:
				for sousserie in serie["children"]:
					node3 = []
					try:
						for division in sousserie["children"]:
							node4 = []
							try:
								for archives in division["children"]:
									link = 'archive/' + str (archives["id"]) +'/detail/'
									arcdict = {"title":archives["title"] , "href": link  ,"tags": [archives["nbrSousDoc"]],"tag":archives["tag"],"key":archives["id"]}
									node4.append(arcdict)
							except:								
								dicav = {"title":'vide'}
								node4.append(dicav)

							link = 'division/' + str(division["id"]) + '/detail/'
							divdict = {"title":division["title"] ,"href":link ,"children": node4,"key":division["id"],"tag":division["tag"]}
							node3.append(divdict)
					except:
						dicdv = {"title":'vide'}
						node3.append(dicdv)

					link = 'sousserie/' + str(sousserie["id"]) + '/detail/'  
					sseriedict = {"title":sousserie["title"] ,"href":link, "children": node3,"key":sousserie["id"],"tag":sousserie["tag"]}
					node2.append(sseriedict)

			except:
				dicssv = {"title":'vide'}
				node2.append(dicssv)

			link = 'serie/' + str (serie["id"]) +'/detail/'
			seriedict = {"title" : serie["title"] , "href": link  , "children":node2,"key":serie["id"],"tag":serie["tag"]}
			json.append(seriedict)

	except:
		#json.append(dicsv)
		pass
		

	return (json)