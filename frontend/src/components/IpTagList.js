import React, {useState, useEffect} from "react";
import axios from 'axios';
import {Link} from "react-router-dom";


const IpTagList = () => {
    const [ipTags, setIpTags] = useState([]);
    const [nextUrl, setNextUrl] = useState(null);
    const [prevUrl, setPrevUrl] = useState(null);
    const [currentPage, setCurrentPage] = useState(1);
    const [filter, setFilter] = useState('');
    const [message, setMessage] = useState('');

    const fetchIpTags = (url = 'http://localhost:8000/api/v1/ip-tags/') => {
        axios.get(url)
        .then(response => {
            setIpTags(response.data.results);
            setNextUrl(response.data.next);
            setPrevUrl(response.data.previous);
        })
            .catch(error => {
                console.error('There was an error fetching the IP tags!', error);
            });
    }


    useEffect(() => {
        fetchIpTags();
    }, []);

    const handleNextPage = () => {
        if (nextUrl) {
            setCurrentPage(currentPage + 1);
            fetchIpTags(nextUrl);
        }
    };

    const handlePrevPage = () => {
        if (prevUrl) {
            setCurrentPage(currentPage - 1);
            fetchIpTags(prevUrl);
        }
    };

    const handleFilterChange = (event) => {
        setFilter(event.target.value);
    };

    const handleDelete = (pk) => {
        axios.delete(`http://localhost:8000/api/v1/ip-tags/${pk}/`)
            .then(response => {
                console.log('IP deleted', pk);
                fetchIpTags();
            })
            .catch(error => {
                console.error('There was an error deleting the IP tag!', error);
            });
    };


    const filteredIpTags = ipTags.filter(ipTag =>
        ipTag.ip_network.includes(filter) || ipTag.tag.includes(filter)
    );

    return (
        <div>
            <h1>IP Tag List</h1>
            <input
                type="text"
                value={filter}
                onChange={handleFilterChange}
                placeholder="Filter by IP network or tag"
                />
            <ul>
                {filteredIpTags.map(ipTag => (
                    <li key={ipTag.id}>
                        {ipTag.ip_network} - {ipTag.tag}
                        <Link to={`/update/${ipTag.id}`}><button>Update</button></Link>
                        <button onClick={() => handleDelete(ipTag.id)}>Delete</button>
                    </li>
                ))}
            </ul>
            <div className="pagination">
                <button onClick={handlePrevPage} disabled={!prevUrl}>Previous</button>
                <span>Page {currentPage}</span>
                <button onClick={handleNextPage} disabled={!nextUrl}>Next</button>
            </div>
            {message && <p>{message}</p>}
        </div>
    );
};

export default IpTagList;