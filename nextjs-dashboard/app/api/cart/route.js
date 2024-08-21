import { NextResponse } from "next/server";
import axios from 'axios';

// Ensure that TOKEN is correctly set in your environment variables
// const TOKEN = '$2b$12$r7c/9yDFIcXAcp8/i1kHb.srrC7AVKdx5BoD6h/uqGT2Lp2SFzo5G'; 
const TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMjUiLCJpZCI6MywiZXhwIjoyMjYzNTQ5NTM0fQ.wOocIrJb34pO7EW7MOMql-NwTGVWgwzPd0OGOUydtbg'; // Use env variable

export async function GET() {
    try {
        // Fetching cart data from the external API
        const response = await axios.get('http://192.168.1.5:5450/cart/fetch', {
            headers: {
                'Authorization': `Bearer ${TOKEN}`,
            },
        });
        // Returning the data as a JSON response
        return NextResponse.json(response.data);
    } catch (error) {
        // Returning a JSON response with error details
        return NextResponse.json({
            error: error.response?.data?.detail || 'An error occurred',
        }, {
            status: error.response?.status || 500,
        });
    }
}
