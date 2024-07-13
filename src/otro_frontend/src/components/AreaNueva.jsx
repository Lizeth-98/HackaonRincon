import { useCanister } from "@connect2ic/react";
import React, { useEffect, useState } from "react";


const Alumnos = () => {
    const [areaICP] = useCanister("otro_backend");
    const [loading, setLoading] = useState("");


    const guardarArea = async (e) => {
        e.preventDefault();
        var ph = parseFloat(e.target[0].value);
        var turbidez = parseFloat(e.target[1].value);

        console.log();
        setLoading("Loading...");

        await areaICP.crearArea(ph, turbidez);
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
                                <input type="text" class="form-control" id="ph" placeholder="Ph" />
                                <input type="text" class="form-control" id="turbidez" placeholder="Turbidez" />
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
