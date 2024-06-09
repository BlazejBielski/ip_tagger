import React, {useState, useEffect} from "react";
import axios from 'axios';
import {Link} from "react-router-dom";
import './IpTagList.css';


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
        <div className="ip-tag-list-container">
            <h1 className="title">IP Tag List</h1>
            <input
                type="text"
                value={filter}
                onChange={handleFilterChange}
                placeholder="Filter by IP network or tag"
                className="filter-input"
                />
            <ul className="ip-tag-list">
                {filteredIpTags.map(ipTag => (
                    <li key={ipTag.id} className="ip-tag-item">
                        <span className="ip-tag-details">{ipTag.ip_network} - {ipTag.tag}</span>
                        <div className="ip-tag-actions">
                                <Link to={`/update/${ipTag.id}`}>
                                    <button className="btn btn-primary">Update</button>
                                </Link>
                            <button className="btn btn-danger" onClick={() => handleDelete(ipTag.id)}>Delete</button>
                            </div>
                    </li>
                    ))}
            </ul>
            <div className="pagination">
                <button onClick={handlePrevPage} disabled={!prevUrl} className="btn btn-secondary">Previous</button>
                <span className="current-page">Page {currentPage}</span>
                <button onClick={handleNextPage} disabled={!nextUrl} className="btn btn-secondary">Next</button>
            </div>
            {message && <p className="message">{message}</p>}
        </div>
    );
};

export default IpTagList;