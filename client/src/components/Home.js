import React, { useState, useEffect } from "react";
import logo from "../static/logo.jpeg";
import "../css/Home.css";

export default function Home() {
    const [baggages, setBaggages] = useState([
        {
            serialID: -1,
            status: "",
            belt: -1,
        },
    ]);

    const [bookingNo, setBookingNo] = useState("");
    const [error, setError] = useState(null);
    const [cache, setCache] = useState("");
    const [skipCount, setSkipCount] = useState(true);

    const handleSubmit = (e) => {
        e.preventDefault();
        setCache(bookingNo);
    };

    const request = () => {
        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
            },
            body: JSON.stringify({
                bookingNo: cache,
            }),
        };

        fetch("https://escendo.azurewebsites.net/api/v1/login", requestOptions)
            .then((response) => {
                return response.json();
            })
            .then((json) => {
                console.log(json);
                setError(json.error);
                setBaggages(json.payload);
            });
    };

    useEffect(() => {
        if (skipCount) setSkipCount(false);
        if (!skipCount) request();
    }, [cache]);

    return (
        <>
            <div className="home-navbar">
                <div className="home-logo">
                    <img src={logo} />
                </div>
            </div>
            <div className="home-content">
                <div className="home-search-bar">
                    <form onSubmit={handleSubmit}>
                        <input
                            type="text"
                            required
                            placeholder="Enter your booking ID"
                            onChange={(e) => setBookingNo(e.target.value)}
                        ></input>
                        <button>
                            <i class="fa-solid fa-magnifying-glass"></i>
                        </button>
                    </form>
                </div>
                <div className="home-payload">
                    <hr className="breaker-line" />
                    <div className="payload-title">
                        <ul>
                            <li>Serial ID</li>
                            <li>Status</li>
                            <li>Belt</li>
                        </ul>
                    </div>
                    <hr className="breaker-line" />
                    <hr></hr>
                    <div className="payload-entries">
                        {error == "error_OK" &&
                            baggages.map((baggage) => (
                                <ul
                                    className="payload-entry-list"
                                    key={baggage.serialID}
                                >
                                    <li>{baggage.serialID}</li>
                                    <li>{baggage.status}</li>
                                    <li>
                                        {baggage.status !=
                                            "Arrived at destination airport" && (
                                            <div>NIL</div>
                                        )}
                                        {baggage.status ==
                                            "Arrived at destination airport" &&
                                            baggage.belt}
                                    </li>
                                </ul>
                            ))}
                        {error == "error_user_not_found" && (
                            <div className="payload-error">
                                Oops! We are unable to find your information!
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </>
    );
}
