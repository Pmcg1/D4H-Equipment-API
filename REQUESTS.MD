# Return a list of inspection result resources

'''GET /team/inspection-results

**Query Parameters:**
completed	boolean
equipment_id	integer [ 1 .. 2147483647 ]
id	integer [ 1 .. 2147483647 ]
inspection_id	integer [ 1 .. 2147483647 ]
location_id	string
limit	integer [ 1 .. 251 ]
offset	integer >= 0
sort	Multiple query params of string


# Return a list of inspection resources

'''GET /team/inspections

**Query Parameters:**
is_active	boolean
equipment_id	integer >= 1
id	Multiple query params of integer >= 1
location_id	string
item_id	integer >= 1
limit	integer [ 1 .. 251 ]
offset	integer >= 0
kind_ids	Multiple query params of integer [ 0 .. 2147483647 ]
team_id	integer >= 1


# Retrieve a single equipment item by its id

'''GET /team/equipment/{equipment_id}

**Path Parameters:**
equipment_id	integer | Required

**Query Parameters:**
location_id	string 


# Update a single equipment item

'''PUT /team/equipment/{equipment_id}

**Path Parameters:**
equipment_id	integer | Required

**FormData Parameters:**
barcode	string
status_id	number
is_critical	boolean
is_monitor	boolean 

# Return a single inspection result resource

'''GET /team/inspection-results/{id}

**Path Parameters:**
id	integer | Required

# Update a single inspection result resource

'''PUT /team/inspection-results/{id}

**Path Parameters:**
id	integer | Required

**Query Parameters:**
status	integer Required
description	string <= 65535 characters
date_completed	string <date> <= now characters


# Return a single inspection resource

'''GET /team/inspections/{inspection_id}

**Path Parameters:**
inspection_id	integer | Required

# Update a single inspection resource

'''PUT /team/inspections/{inspection_id}

**Path Parameters:**
inspection_id	integer | Required

**formData Parameters:**
title	string
description	string
active	boolean
gear_parent_id	integer >= 1
all_kinds	boolean
location_id	integer >= 1
member_id	integer >= 1
interval_value	integer
interval_unit	string
reminder_value	integer
reminder_unit	string


# List of inspections related to an equipment item

'''GET /team/equipment/{equipment_id}/inspections

**Path Parameters:**
equipment_id	integer | Required

**Query Parameters:**
limit	integer [ 1 .. 251 ]
offset	integer >= 0 

# Return the items to be inspected within an inspection resource

'''GET /team/inspections/{inspection_id}/items

**Path Parameters:**
inspection_id	integer | Required

**Query Parameters:**
location_id	string
completed	boolean
limit	integer [ 1 .. 251 ] 
offset	integer >= 0 

# Return the equipment to be inspected within an inspection resource

'''GET /team/inspections/{inspection_id}/equipment

**Path Parameters:**
inspection_id	integer | Required

**Query Parameters:**
ref	string
location_id	string
completed	boolean
limit	integer [ 1 .. 251 ]
offset	integer >= 0 

# Return a single item to be inspected within an inspection resource

'''GET /team/inspections/{inspection_id}/items/{item_id}

**Path Parameters:**
inspection_id	integer | Required
item_id	integer >= 1 

# Update a single inspection instance within an inspection resource

'''PUT /team/inspections/{inspection_id}/items/{item_id}

**Path Parameters:**
inspection_id	integer | Required
item_id	integer >= 1

**FormData Parameters:**
status	number Required
description	string
date_completed	string <date>