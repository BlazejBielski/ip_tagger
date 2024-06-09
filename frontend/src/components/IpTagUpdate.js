// src/components/IpTagUpdate.js
import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from 'axios';

const IpTagUpdate = () => {
    const { pk } = useParams();
    const navigate = useNavigate();
    const [ipNetwork, setIpNetwork] = useState('');
    const [tag, setTag] = useState('');
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get(`http://localhost:8000/api/v1/ip-tags/${pk}/`)
            .then(response => {
                setIpNetwork(response.data.ip_network);
                setTag(response.data.tag);
            })
            .catch(error => {
                console.error('There was an error fetching the IP tag!', error);
                setMessage('There was an error fetching the IP tag.');
            });
    }, [pk]);

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.put(`http://localhost:8000/api/v1/ip-tags/${pk}/`, { ip_network: ipNetwork, tag: tag })
            .then(response => {
                console.log('IP tag updated:', response.data);
                setMessage(`IP Tag Updated: ${response.data.ip_network} - ${response.data.tag}`);
                navigate('/list');
            })
            .catch(error => {
                console.error('There was an error updating the IP tag!', error);
                setMessage('There was an error updating the IP tag.');
            });
    };

    return (
        <div>
            <h1>Update IP Tag</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>IP Network:</label>
                    <input type="text" value={ipNetwork} onChange={e => setIpNetwork(e.target.value)} />
                </div>
                <div>
                    <label>Tag:</label>
                    <input type="text" value={tag} onChange={e => setTag(e.target.value)} />
                </div>
                <button type="submit">Update</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default IpTagUpdate;
