import { useCanister } from "@connect2ic/react";
import React, { useEffect, useState } from "react";


const Alumnos = () => {
    const [areaICP] = useCanister("otro_backend");
    const [loading, setLoading] = useState("");


    const guardarArea = async (e) => {
        e.preventDefault();
        var ph = parseFloat(e.target[0].value);
        var humedad = parseFloat(e.target[1].value);
        var nitrogeno = parseFloat(e.target[2].value);
        var fosforo = parseFloat(e.target[3].value);
        var potasio = parseFloat(e.target[4].value);

        console.log();
        setLoading("Loading...");

        await areaICP.crearArea(ph, humedad, nitrogeno, fosforo, potasio);
        setLoading("");

        {
            document.getElementById('btnListaAreas').click();
        }


    }


    return (
        <div className="row  mt-5">
            <div className="col">
                {loading != ""
                    ?
                    <div className="alert alert-primary">{loading}</div>
                    :
                    <div></div>
                }
                <div class="card">
                    <div class="card-header">
                        Registrar alumno
                    </div>
                    <div class="card-body">
                        <form class="form" onSubmit={guardarArea}>
                            <div class="mb-3">
                                <label for="nombre" class="form-label">Alumno</label>
                                <input type="text" class="form-control" id="ph" placeholder="Matrícula" />
                                <input type="text" class="form-control" id="humedad" placeholder="Matemáticas" />
                                <input type="text" class="form-control" id="nitrogeno" placeholder="Español" />
                                <input type="text" class="form-control" id="fosforo" placeholder="Química" />
                                <input type="text" class="form-control" id="potasio" placeholder="Inglés" />
                            </div>

                            <input type="submit" class="btn btn-success" value="Agregar" />
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}


export default Alumnos