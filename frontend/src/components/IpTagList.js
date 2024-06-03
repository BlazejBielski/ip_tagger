import React, {useState, useEffect} from "react";
import axios from 'axios';


const IpTagList = () => {
    const [ipTags, setIpTags] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/v1/ip-tags/')
            .then(response => {
                console.log('API Response:', response.data); // Dodaj to, aby zobaczyć dane w konsoli
                setIpTags(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the IP tags!', error);
            });
    }, []);

    return (
        <div>
            <h1>IP Tag List</h1>
            <ul>
                {ipTags.map(ipTag => (
                    <li key={ipTag.id}>
                        {ipTag.ip_network} - {ipTag.tag}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default IpTagList;