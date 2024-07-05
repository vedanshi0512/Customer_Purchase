from load_data import load_data

def interactive_sql():
    """Allows user to input SQL queries interactively."""
    print("Welcome to Interactive SQL Query Tool.")
    print("Enter your SQL query below. Type 'exit' to quit.")
    
    while True:
        user_input = input("SQL> ")
        
        if user_input.lower() == 'exit':
            print("Exiting Interactive SQL Query Tool.")
            break
        
        try:
            result_df = load_data(user_input)
            print(result_df.to_string(index=False)) 
        except Exception as e:
            print(f"Error executing SQL query: {str(e)}")

if __name__ == "__main__":
    interactive_sql()
