import React, {useState} from "react";
import axios from 'axios';
import './IpTagForm.css';


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
        <div className="container mt-4 ip-tag-form-container">
            <h1 className="text-center">Create IP Tag</h1>
            <form onSubmit={handleSubmit} className="ip-tag-form">
                <div className="form-group">
                    <label>IP Network:</label>
                    <input type="text" value={ipNetwork} onChange={e => setIpNetwork(e.target.value)} className="form-control" />
                </div>
                <div className="form-group">
                    <label>Tag:</label>
                    <input type="text" value={tag} onChange={e => setTag(e.target.value)} className="form-control" />
                </div>
                <button type="submit" className="btn btn-primary mt-3" >Create</button>
            </form>
            {message && <p className="text-center mt-3 message">{message}</p>}
        </div>
        );
        };

export default IpTagCreate;