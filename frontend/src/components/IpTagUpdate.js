// src/components/IpTagUpdate.js
import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from 'axios';
import './IpTagForm.css';

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
        <div className="container mt-4 ip-tag-form-container">
            <h1 className="text-center">Update IP Tag</h1>
            <form onSubmit={handleSubmit} className="ip-tag-form">
                <div className="form-group">
                    <label>IP Network:</label>
                    <input type="text" value={ipNetwork} onChange={e => setIpNetwork(e.target.value)} className="form-control" />
                </div>
                <div className="form-group">
                    <label>Tag:</label>
                    <input type="text" value={tag} onChange={e => setTag(e.target.value)} className="form-control" />
                </div>
                <button type="submit" className="btn btn-primary mt-3">Update</button>
            </form>
            {message && <p className="text-center mt-3 message">{message}</p>}
        </div>
    );
};

export default IpTagUpdate;
