import React, {useState, useEffect} from "react";
import axios from 'axios';


const IpTagList = () => {
    const [ipTags, setIpTags] = useState([]);
    const [nextUrl, setNextUrl] = useState(null);
    const [prevUrl, setPrevUrl] = useState(null);
    const [currentPage, setCurrentPage] = useState(1);

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
            <div className="pagination">
                <button onClick={handlePrevPage} disabled={!prevUrl}>Previous</button>
                <span>Page {currentPage}</span>
                <button onClick={handleNextPage} disabled={!nextUrl}>Next</button>
            </div>
        </div>
    );
};

export default IpTagList;