import React, { useEffect, useState } from 'react';

function App() {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('https://jsonplaceholder.typicode.com/posts')
            .then(response => response.json())
            .then(data => setData(data));
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            <ul>{data.slice(0, 5).map(post => <li key={post.id}>{post.title}</li>)}</ul>
        </div>
    );
}

export default App;