// frontend/src/App.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/users')
            .then(response => {
                setUsers(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the data!', error);
            });
    }, []);

    return (
        <div className="App">
            <h1>User List</h1>
            <ul>
                {users.map((user, index) => (
                    <li key={index}>{user.name} - {user.age} years old</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
