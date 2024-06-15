import sqlite3


def other():
    # Step 6: Update a row
    update_row_query = '''
    UPDATE users SET age = ? WHERE name = ?;
    '''
    cursor.execute(update_row_query, (31, 'John Doe'))
    print("Row updated successfully.")


    # Step 8: Delete a row
    delete_row_query = '''
    DELETE FROM users WHERE name = ?;
    '''
    cursor.execute(delete_row_query, ('Jane Smith',))
    print("Row deleted successfully.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()


#def isExistKey():

def execute_SelectAll(table_name):
    select_all_query = '''
    SELECT * FROM {1};
    '''

    select_all_query = select_all_query.replace("{1}", table_name)

    cursor.execute(select_all_query)
    rows = cursor.fetchall()

    return rows

def execute_SelectByKey(table_name, kye_colunm_name, kye_colunm_value):
    select_all_query = '''
    SELECT * FROM {1} WHERE {2} = '{3}';
    '''

    select_all_query = select_all_query.replace("{1}", table_name)
    select_all_query = select_all_query.replace("{2}", kye_colunm_name)
    select_all_query = select_all_query.replace("{3}", kye_colunm_value)
    
    print("execute_SelectByKey -> " + select_all_query)
    cursor.execute(select_all_query)
    rows = cursor.fetchall()

    return rows


def execute_DropTable(table_name):

    # Step 2: Drop table
    drop_table_query = '''
    DROP TABLE IF EXISTS {1};
    '''

    drop_table_query = drop_table_query.replace("{1}", table_name)
    
    # Drop tableを使いたい場合は以下のコメントアウトを外す
    cursor.execute(drop_table_query)
    print("Table 'users' dropped successfully.")

def execute_AlterTable():

    alter_table_query = '''
    ALTER TABLE users ADD COLUMN email TEXT;
    '''
    cursor.execute(alter_table_query)
    print("Table 'users' altered successfully to add 'email' column.")

def execute_Insert():
    # Step 5: Create a row (insert data)
    create_row_query = '''
    INSERT INTO users (name, age, email) VALUES (?, ?, ?);
    '''
    cursor.execute(create_row_query, ('John Doe', 30, 'john.doe@example.com'))
    print("Row created successfully.")

    # Step 7: Insert additional rows
    additional_rows = [
        ('Jane Smith', 25, 'jane.smith@example.com'),
        ('Emily Johnson', 29, 'emily.johnson@example.com')
    ]
    cursor.executemany(create_row_query, additional_rows)
    print("Additional rows inserted successfully.")






def init_Database():
    # Step 1: Create table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    print("Table 'users' created successfully.")



if __name__ == "__main__":
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    init_Database()

    # checked
    print(execute_SelectAll('users'))

    selectByKey = execute_SelectByKey('users', 'email', 'john.doe@example.com')
    print(len(selectByKey))

    other()
