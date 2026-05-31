# Smart Inventory Management System

# Core Storage structures
# dict format: { product_id: {"name": str, "category": str, "qty": int, "price": float, "supplier": str} }
inventory = {} 
categories_set = set() # set tracking unique categories

def add_product():
    print("\n--- ➕ Add Product ---")
    p_id = input("Enter unique Product ID: ").strip()
    if p_id in inventory:
        print("[Error] A product with this ID already exists.")
        return
        
    name = input("Enter Product Name: ").strip()
    category = input("Enter Category: ").strip()
    try:
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price (₹): "))
    except ValueError:
        print("[Error] Invalid numeric data input.")
        return
    supplier = input("Enter Supplier Name: ").strip()
    
    # Store record inside our master tracking dictionary
    inventory[p_id] = {
        "name": name,
        "category": category,
        "qty": qty,
        "price": price,
        "supplier": supplier
    }
    # Category Management requirement using Sets
    categories_set.add(category)
    print(f"Success: '{name}' added to stock safely.")

def update_inventory():
    print("\n--- 🔄 Update Inventory ---")
    p_id = input("Enter Product ID to update: ").strip()
    if p_id not in inventory:
        print("[Error] Product ID not found.")
        return
        
    print("Leave field blank to keep current value.")
    qty_input = input(f"Enter new quantity (Current: {inventory[p_id]['qty']}): ").strip()
    price_input = input(f"Enter new price (Current: ₹{inventory[p_id]['price']}): ").strip()
    
    try:
        if qty_input:
            inventory[p_id]['qty'] = int(qty_input)
        if price_input:
            inventory[p_id]['price'] = float(price_input)
        print("Success: Product record metrics modified successfully.")
    except ValueError:
        print("[Error] Numerical conversion error. Updates aborted.")

def search_product():
    print("\n--- 🔍 Search Product ---")
    criterion = input("Search by Product (1) ID or (2) Name? Enter option (1/2): ").strip()
    
    # Using lists to accumulate matches
    search_results = []
    
    if criterion == '1':
        p_id = input("Enter Product ID: ").strip()
        if p_id in inventory:
            search_results.append((p_id, inventory[p_id]))
    elif criterion == '2':
        search_name = input("Enter Product Name (Case-Insensitive): ").strip().lower()
        for k, v in inventory.items():
            if search_name in v['name'].lower():
                search_results.append((k, v))
    else:
        print("[Error] Invalid option selected.")
        return

    if not search_results:
        print("No matching items found in inventory.")
    else:
        print_table(search_results)

def display_inventory():
    print("\n--- 📦 Current Inventory Stock View ---")
    if not inventory:
        print("Inventory layout is empty.")
        return
    # Convert whole dict items to a flat array list for printing
    print_table(list(inventory.items()))

def delete_product():
    print("\n--- 🗑️ Delete Product ---")
    p_id = input("Enter Product ID to remove: ").strip()
    if p_id in inventory:
        removed_item = inventory.pop(p_id)
        print(f"Success: Product '{removed_item['name']}' removed from catalog.")
        
        # Recalculate unique categories set dynamically
        global categories_set
        categories_set = {item['category'] for item in inventory.values()}
    else:
        print("[Error] Target Product ID not recognized.")

def check_alerts():
    print("\n--- ⚠️ System Alerts Engine ---")
    try:
        threshold = input("Enter Low Stock threshold criteria limit (Press Enter for Default 10): ").strip()
        threshold = int(threshold) if threshold else 10
    except ValueError:
        print("[Error] Invalid input. Resetting system parameters to default 10.")
        threshold = 10

    out_of_stock = []
    low_stock = []

    for k, v in inventory.items():
        if v['qty'] == 0:
            out_of_stock.append((k, v))
        elif v['qty'] < threshold:
            low_stock.append((k, v))

    print("\n🚨 OUT OF STOCK ALERTS (Quantity = 0):")
    if out_of_stock:
        print_table(out_of_stock)
    else:
        print("   Clear. No critical stock-outs identified.")

    print(f"\n🔸 LOW STOCK ALERTS (Quantity < {threshold}):")
    if low_stock:
        print_table(low_stock)
    else:
        print("   Clear. All item volumes above target buffer profiles.")

def category_management():
    print("\n--- 🗂️ Category Management ---")
    print(f"Total Unique Categories Registered: {len(categories_set)}")
    for index, cat in enumerate(categories_set, 1):
        print(f" {index}. Category Scope: {cat}")

def generate_inventory_report():
    print("\n--- 📊 Inventory Executive Summary Report ---")
    if not inventory:
        print("No analytical aggregates available. Inventory data structurally empty.")
        return

    total_items = 0
    total_valuation = 0.0
    category_summary = {} # Temp mapping breakdown metric
    snapshots_list = [] # Tuple list tracking history snapshots

    for k, v in inventory.items():
        qty = v['qty']
        item_value = qty * v['price']
        
        total_items += qty
        total_valuation += item_value
        
        # Categorical summaries computations
        cat = v['category']
        category_summary[cat] = category_summary.get(cat, 0.0) + item_value
        
        # tuple (product snapshots tracking data structures)
        snapshot = (k, v['name'], qty, item_value)
        snapshots_list.append(snapshot)

    print(f"Global Distinct Item Types Managed: {len(inventory)}")
    print(f"Total Cumulative Stock Volume:      {total_items} units")
    print(f"Gross Asset Inventory Valuation:    ₹{total_valuation:,.2f}")
    
    print("\nCategory-wise Asset Valuation Summary:")
    for cat, val in category_summary.items():
        print(f" 🔹 Category '{cat:<15}': Total Holding Value: ₹{val:,.2f}")

def print_table(product_list):
    """Helper method formatting lists into cleanly spaced terminal tables."""
    header = f"{'ID':<8} | {'Product Name':<18} | {'Category':<15} | {'Qty':<6} | {'Price':<10} | {'Supplier':<15}"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for p_id, info in product_list:
        print(f"{p_id:<8} | {info['name']:<18} | {info['category']:<15} | {info['qty']:<6} | ₹{info['price']:<9,.2f} | {info['supplier']:<15}")
    print("-" * len(header))

def main():
    while True:
        print("\n=============================================")
        print("      🛡️ SMART INVENTORY MANAGEMENT SYSTEM   ")
        print("=============================================")
        print("1. Add New Product Record")
        print("2. Update Existing Inventory Metric")
        print("3. Search Product (ID / Name Case-Insensitive)")
        print("4. Display Inventory (Formatted Table)")
        print("5. Delete Product Entry from Database")
        print("6. Run Low & Out-of-Stock Alert Engine")
        print("7. Track Unique Categories (Sets Tracker)")
        print("8. Compile Asset Valuation Financial Report")
        print("9. Terminate Application Portal")
        print("=============================================")
        
        choice = input("Select a management workflow routine (1-9): ").strip()
        if choice == '1': add_product()
        elif choice == '2': update_inventory()
        elif choice == '3': search_product()
        elif choice == '4': display_inventory()
        elif choice == '5': delete_product()
        elif choice == '6': check_alerts()
        elif choice == '7': category_management()
        elif choice == '8': generate_inventory_report()
        elif choice == '9':
            print("\nShutting down core engine array. Workspace states saved. Goodbye!")
            break
        else:
            print("\n[Invalid Code] Select an option from 1 to 9.")

if __name__ == "__main__":
    main()

Output:
=============================================
      🛡️ SMART INVENTORY MANAGEMENT SYSTEM   
=============================================
1. Add New Product Record
2. Update Existing Inventory Metric
3. Search Product (ID / Name Case-Insensitive)
4. Display Inventory (Formatted Table)
5. Delete Product Entry from Database
6. Run Low & Out-of-Stock Alert Engine
7. Track Unique Categories (Sets Tracker)
8. Compile Asset Valuation Financial Report
9. Terminate Application Portal
=============================================
Select a management workflow routine (1-9): 4

--- 📦 Current Inventory Stock View ---
Inventory layout is empty.

=============================================
      🛡️ SMART INVENTORY MANAGEMENT SYSTEM   
=============================================
1. Add New Product Record
2. Update Existing Inventory Metric
3. Search Product (ID / Name Case-Insensitive)
4. Display Inventory (Formatted Table)
5. Delete Product Entry from Database
6. Run Low & Out-of-Stock Alert Engine
7. Track Unique Categories (Sets Tracker)
8. Compile Asset Valuation Financial Report
9. Terminate Application Portal
=============================================
Select a management workflow routine (1-9): 6

--- ⚠️ System Alerts Engine ---
Enter Low Stock threshold criteria limit (Press Enter for Default 10): 8

🚨 OUT OF STOCK ALERTS (Quantity = 0):
   Clear. No critical stock-outs identified.

🔸 LOW STOCK ALERTS (Quantity < 8):
   Clear. All item volumes above target buffer profiles.

=============================================
      🛡️ SMART INVENTORY MANAGEMENT SYSTEM   
=============================================
1. Add New Product Record
2. Update Existing Inventory Metric
3. Search Product (ID / Name Case-Insensitive)
4. Display Inventory (Formatted Table)
5. Delete Product Entry from Database
6. Run Low & Out-of-Stock Alert Engine
7. Track Unique Categories (Sets Tracker)
8. Compile Asset Valuation Financial Report
9. Terminate Application Portal
=============================================
Select a management workflow routine (1-9): 8

--- 📊 Inventory Executive Summary Report ---
No analytical aggregates available. Inventory data structurally empty.

=============================================
      🛡️ SMART INVENTORY MANAGEMENT SYSTEM   
=============================================
1. Add New Product Record
2. Update Existing Inventory Metric
3. Search Product (ID / Name Case-Insensitive)
4. Display Inventory (Formatted Table)
5. Delete Product Entry from Database
6. Run Low & Out-of-Stock Alert Engine
7. Track Unique Categories (Sets Tracker)
8. Compile Asset Valuation Financial Report
9. Terminate Application Portal
=============================================
Select a management workflow routine (1-9): 9
