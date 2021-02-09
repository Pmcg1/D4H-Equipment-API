Return a list of inspection result resources

	GET /team/inspection-results
	

Return a list of inspection resources

	GET /team/inspections
	

Retrieve a single equipment item by its id

	GET /team/equipment/{equipment_id}
	

Update a single equipment item

	PUT /team/equipment/{equipment_id}
	
	
Return a single inspection result resource

	GET /team/inspection-results/{id}
	

Update a single inspection result resource

	PUT /team/inspection-results/{id}
	

Return a single inspection resource
	
	GET /team/inspections/{inspection_id}
	

Update a single inspection resource

	PUT /team/inspections/{inspection_id}
	
	
List of inspections related to an equipment item

	GET /team/equipment/{equipment_id}/inspections
	
	
Return the items to be inspected within an inspection resource

	GET /team/inspections/{inspection_id}/items
	

Return the equipment to be inspected within an inspection resource

	GET /team/inspections/{inspection_id}/equipment
	
	
Return a single item to be inspected within an inspection resource

	GET /team/inspections/{inspection_id}/items/{item_id}
	

Update a single inspection instance within an inspection resource

	PUT /team/inspections/{inspection_id}/items/{item_id}
	
	


