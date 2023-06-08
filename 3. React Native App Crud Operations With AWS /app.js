import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, TouchableOpacity, TextInput, StyleSheet } from 'react-native';
import axios from 'axios';

const App = () => {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState('');
  const [completed, setCompleted] = useState(false);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      const response = await axios.get('https://38g303h2uh.execute-api.ap-south-1.amazonaws.com/test', {
        headers: {
          authorizationToken: 'RedshiftAws'
        }
      });
      setTodos(response.data);
      console.log(response.data, "Response");
    } catch (error) {
      console.error(error);
    }
  };

  let counter=todos.length;
const getId = () => {
  const id = counter+1;
  counter += 1;
  return id;
};
  const addTodo = async () => {
    try {
      const newTodo = {
        id: getId(),
        title,
        completed
      };
  
      const response = await axios.post('https://38g303h2uh.execute-api.ap-south-1.amazonaws.com/test', newTodo,{
        headers: {
          authorizationToken: 'RedshiftAws'
        }
      });
      setTodos([...todos, response.data]);
      setTitle('');
      setCompleted(false);
      fetchTodos();
    } catch (error) {
      console.error(error);
    }
  };

  const updateTodo = async (id, updatedTodo) => {
    try {
      await axios.put(`https://38g303h2uh.execute-api.ap-south-1.amazonaws.com/test/?id=${id}`, updatedTodo,{
        headers: {
          authorizationToken: 'RedshiftAws'
        }
      });
      setTodos(todos.map((todo) => (todo.id === id ? { ...todo, ...updatedTodo } : todo)));
    } catch (error) {
      console.error(error);
    }
  };

  const deleteTodo = async (id) => {
    try {
      await axios.delete(`https://38g303h2uh.execute-api.ap-south-1.amazonaws.com/test/?id=${id}`,{
        headers: {
          authorizationToken: 'RedshiftAws'
        }
      });
      setTodos(todos.filter((todo) => todo.id !== id));
    } catch (error) {
      console.error(error);
    }
  };

  const renderItem = ({ item }) => (
    <View style={styles.todoContainer}>
      <Text style={styles.todoTitle}>{item.title}</Text>
      <Text style={styles.todoStatus}>{item.completed ? 'Completed' : 'Pending'}</Text>
      <TouchableOpacity
        style={styles.updateButton}
        onPress={() => updateTodo(item.id, { completed: !item.completed })}
      >
        <Text style={styles.buttonText}>
          {item.completed ? 'Mark as Pending' : 'Mark as Completed'}
        </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.deleteButton} onPress={() => deleteTodo(item.id)}>
        <Text style={styles.buttonText}>Delete</Text>
      </TouchableOpacity>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Todo List</Text>
      <View style={styles.formContainer}>
        <TextInput
          style={styles.input}
          placeholder="Title"
          value={title}
          onChangeText={setTitle}
        />
        <TouchableOpacity style={styles.addButton} onPress={addTodo}>
          <Text style={styles.buttonText}>Add Todo</Text>
        </TouchableOpacity>
      </View>
      <FlatList
        data={todos}
        renderItem={renderItem}
        keyExtractor={(item) => item.id?.toString() || Math.random().toString()}
      />
    </View>
  );
};

export default App

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  formContainer: {
    marginBottom: 16,
  },
  input: {
    height: 40,
    borderWidth: 1,
    borderColor: '#ccc',
    paddingHorizontal: 10,
    marginBottom: 8,
  },
  addButton: {
    backgroundColor: 'blue',
    padding: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
  todoContainer: {
    marginBottom: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  todoTitle: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  todoStatus: {
    color: 'gray',
  },
  updateButton: {
    marginTop: 8,
    backgroundColor: 'green',
    padding: 8,
    alignItems: 'center',
    justifyContent: 'center',
  },
  deleteButton: {
    marginTop: 8,
    backgroundColor: 'red',
    padding: 8,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
