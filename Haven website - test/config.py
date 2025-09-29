// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBwBBfN5LG6RFRezR5cBfcWKv9iKzIdAvA",
  authDomain: "green-haven-tut.firebaseapp.com",
  databaseURL: "https://green-haven-tut-default-rtdb.firebaseio.com",
  projectId: "green-haven-tut",
  storageBucket: "green-haven-tut.firebasestorage.app",
  messagingSenderId: "30246624131",
  appId: "1:30246624131:web:e5e151aa0672721512f4b6"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);