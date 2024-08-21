
import { NextResponse } from 'next/server';
import axios from 'axios';

export async function GET() {
  const get="Get request of api/books";
  return NextResponse.json(get);
  // try {
  //   const response = await axios.get('http://192.168.1.10:5427/book/books'); // Replace with your FastAPI endpoint
  //   return NextResponse.json(response.data);
  // } catch (error) {
  //   return NextResponse.json({ error: error.message }, { status: error.response?.status || 500 });
  // }
}

