from insurance.manager import CustomerManager
from insurance.exceptions import CustomerNotFoundError, FileReadError, FileWriteError

def main():
    try:
        manager = CustomerManager()

        print("\n📋 Current Customers:")
        manager.list_customers()

        print("\n➕ Adding a new customer...")
        manager.add_customer(3, "Charlie", "POL67890", "Health", 1800)

        print("\n🔍 Searching for customer POL54321...")
        try:
            c = manager.find_customer("POL54321")
            print("✅ Found:", c)
        except CustomerNotFoundError as e:
            print(e)

        print("\n✏️ Updating Bob's policy...")
        manager.update_customer("POL54321", new_premium=2000, new_type="Life+Vehicle")

        print("\n⚰️ Marking Bob as Deceased...")
        manager.update_customer("POL54321", new_status="Deceased")

        print("\n🗑️ Deleting Alice...")
        manager.delete_customer("POL12345")

        print("\n📋 Final Customers:")
        manager.list_customers()

        print("\n💾 Saving to file...")
        manager.save()

    except (FileReadError, FileWriteError) as e:
        print(e)

if __name__ == "__main__":
    main()
    