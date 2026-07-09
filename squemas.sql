--
-- PostgreSQL database dump
--

\restrict KqnAPfZ9M2DoCTIgMhhd9iD4hzFXanDaS3dwPhdQ4VguGsXfHEeuQyKVTgJtbep

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.3

-- Started on 2026-07-09 01:09:19

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 17562)
-- Name: artistas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.artistas (
    id_artista integer NOT NULL,
    nombre character varying(100) NOT NULL,
    pais character varying(50),
    genero character varying(50)
);


ALTER TABLE public.artistas OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 17561)
-- Name: artistas_id_artista_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.artistas_id_artista_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.artistas_id_artista_seq OWNER TO postgres;

--
-- TOC entry 5024 (class 0 OID 0)
-- Dependencies: 219
-- Name: artistas_id_artista_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.artistas_id_artista_seq OWNED BY public.artistas.id_artista;


--
-- TOC entry 222 (class 1259 OID 17571)
-- Name: canciones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.canciones (
    id_cancion integer NOT NULL,
    titulo character varying(100) NOT NULL,
    duracion character varying(10),
    anio integer,
    id_artista integer
);


ALTER TABLE public.canciones OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 17570)
-- Name: canciones_id_cancion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.canciones_id_cancion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.canciones_id_cancion_seq OWNER TO postgres;

--
-- TOC entry 5025 (class 0 OID 0)
-- Dependencies: 221
-- Name: canciones_id_cancion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.canciones_id_cancion_seq OWNED BY public.canciones.id_cancion;


--
-- TOC entry 4861 (class 2604 OID 17565)
-- Name: artistas id_artista; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.artistas ALTER COLUMN id_artista SET DEFAULT nextval('public.artistas_id_artista_seq'::regclass);


--
-- TOC entry 4862 (class 2604 OID 17574)
-- Name: canciones id_cancion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.canciones ALTER COLUMN id_cancion SET DEFAULT nextval('public.canciones_id_cancion_seq'::regclass);


--
-- TOC entry 5016 (class 0 OID 17562)
-- Dependencies: 220
-- Data for Name: artistas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.artistas (id_artista, nombre, pais, genero) FROM stdin;
3	Juan Luis Guerra	Republica Dominicana	Bachataa
\.


--
-- TOC entry 5018 (class 0 OID 17571)
-- Dependencies: 222
-- Data for Name: canciones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.canciones (id_cancion, titulo, duracion, anio, id_artista) FROM stdin;
3	Bachata Rosa	3:50	1990	3
\.


--
-- TOC entry 5026 (class 0 OID 0)
-- Dependencies: 219
-- Name: artistas_id_artista_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.artistas_id_artista_seq', 6, true);


--
-- TOC entry 5027 (class 0 OID 0)
-- Dependencies: 221
-- Name: canciones_id_cancion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.canciones_id_cancion_seq', 3, true);


--
-- TOC entry 4864 (class 2606 OID 17569)
-- Name: artistas artistas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.artistas
    ADD CONSTRAINT artistas_pkey PRIMARY KEY (id_artista);


--
-- TOC entry 4866 (class 2606 OID 17578)
-- Name: canciones canciones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.canciones
    ADD CONSTRAINT canciones_pkey PRIMARY KEY (id_cancion);


--
-- TOC entry 4867 (class 2606 OID 17585)
-- Name: canciones canciones_id_artista_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.canciones
    ADD CONSTRAINT canciones_id_artista_fkey FOREIGN KEY (id_artista) REFERENCES public.artistas(id_artista) ON DELETE CASCADE;


-- Completed on 2026-07-09 01:09:19

--
-- PostgreSQL database dump complete
--

\unrestrict KqnAPfZ9M2DoCTIgMhhd9iD4hzFXanDaS3dwPhdQ4VguGsXfHEeuQyKVTgJtbep

