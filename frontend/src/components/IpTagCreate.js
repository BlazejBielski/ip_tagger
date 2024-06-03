import React, {useState} from "react";
import axios from 'axios';


const IpTagCreate = () => {
    const [ipNetwork, setIpNetwork] = useState('');
    const [tag, setTag] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.post('http://localhost:8000/api/v1/ip-tags/', {ip_network: ipNetwork, tag: tag})
            .then(response => {
                console.log('IP tag created:', response.data);
                setIpNetwork('');
                setTag('');
                setMessage(`IP Tag Created: ${response.data.ip_network} - ${response.data.tag}`);
            })
            .catch(error => {
                console.error('There was an error creating the IP tag!', error);
                setMessage('There was an error creating the IP tag.');
            });
    };

    return (
        <div>
            <h1>Create IP Tag</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>IP Network:</label>
                    <input type="text" value={ipNetwork} onChange={e => setIpNetwork(e.target.value)}/>
                </div>
                <div>
                    <label>Tag:</label>
                    <input type="text" value={tag} onChange={e => setTag(e.target.value)}/>
                </div>
                <button type="submit">Create</button>
            </form>
            {message && <p>{message}</p>}
        </div>
        );
        };

export default IpTagCreate;