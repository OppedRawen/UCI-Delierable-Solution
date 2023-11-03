import "./App.css";
import React,{useEffect,useState} from "react";
import Quote from "./components/Quote";
import axios from "axios";
import {BsBookmarkCheck} from "react-icons/bs";
function App() {

	const [quotes,setQuotes] = useState([]);

	useEffect(()=>{
		axios.get('/api/quote')
			.then(res=>{
				setQuotes(res.data);
			})
			.catch(error=>console.error(error));
	},[]);

	return (

		<div className="App">
			{/* TODO: include an icon for the quote book */}
			M
			<BsBookmarkCheck className="icon" />
			<h1>Hack @ UCI Tech Deliverable</h1>

			<h2>Submit a quote</h2>
			{/* TODO: implement custom form submission logic to not refresh the page */}
			<form action="/api/quote" method="post" className="qoute-form">
				<label htmlFor="input-name">Name</label>
				<input type="text" name="name" id="input-name" required />
				<label htmlFor="input-message">Quote</label>
				<input type="text" name="message" id="input-message" required />
				<button type="submit">Submit</button>
			</form>

			<h2>Previous Quotes</h2>
			{/* TODO: Display the actual quotes from the database */}
{/* 
			<div className="messages">
				
				<p>Peter Anteater</p>
				<p>Zot Zot Zot!</p>
				<p>Every day</p>
			</div> */}
			<div className="quotes-list">
    {quotes.map((quote, index) => (
        <Quote key={index} name={quote.name} message={quote.message} time={quote.time} />
	
    ))}
	
</div>
		</div>
	);
}

export default App;
