import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import React from 'react'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppMenu } from './components/AppMenu'
// import { DentistShowAll } from './components/Dentists/DentistShowAll'
import { AppHome } from './components/AppHome'
import { PatientShowAll } from './components/Patients/PatientsShowAll'
import { PatientDetail } from './components/Patients/PatientDetail'
import { PatientDelete } from './components/Patients/PatientDelete'
import { PatientAdd } from './components/Patients/PatientAdd'
import { PatientUpdate } from './components/Patients/PatientUpdate'
import { PatientShowOlderThan18 } from './components/Patients/PatientShowOlderThan18'

// function App() {

//     return (
//       <React.Fragment>
//         <Router>
//           <AppMenu/>
//           <Routes>
//             <Route path="/" element={<AppHome/>} />
//             <Route path="/patient/" element={<PatientShowAll />} />
//             <Route path="/patient/:patientId" element={<PatientDetail />} />
//             <Route path="/patient/:patientId/delete" element={<PatientDelete />} />
//             <Route path="/patient/add" element={<PatientAdd />} /> 
//             <Route path="/patient/:patientId/edit" element={<PatientUpdate />} />
//           </Routes>
//         </Router>
//       </React.Fragment>
//     )
// }

// export default App;


function App() {
  const [count, setCount] = useState(0);

  return (
    <React.Fragment>
      <Router>
        <AppMenu/>
        <Routes>
          <Route path="/" element={<AppHome />} />
          <Route path="/patient/" element={<PatientShowAll />} />
          <Route path="/patient/:patientId" element={<PatientDetail />} />
          <Route path="/patient/:patientId/delete" element={<PatientDelete />} />
          <Route path="/patient/add" element={<PatientAdd />} /> 
          <Route path="/patient/:patientId/edit" element={<PatientUpdate />} />
          <Route path="/patient/older-than-18" element={<PatientShowOlderThan18 />} />
        </Routes>
      </Router>
    </React.Fragment>

  )
}

export default App;