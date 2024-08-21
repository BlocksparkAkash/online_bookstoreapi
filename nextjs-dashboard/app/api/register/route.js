import { NextResponse } from "next/server";

    export async function GET(request)
        {
            return NextResponse.json({message: "GET request is fired"})
        }

import axios from 'axios';



export async function POST(req) {
  try {
    const body = await req.json();
    const response = await axios.post('http://192.168.1.5:5450/auth/register', body);
    return new Response(JSON.stringify(response.data), {
      status: response.status,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: error.response?.status || 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}


// export async function POST(request) {
//     // Your registration logic
//     return new Response(JSON.stringify({ message: 'Registration successful' }), { status: 200 });
//   }
