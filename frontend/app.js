function App() {
  const [persons, setPersons] = React.useState([]);
  const [name, setName] = React.useState('');
  const [email, setEmail] = React.useState('');
  const [phone, setPhone] = React.useState('');

  const loadData = () => {
    fetch('../backend/index.php')
      .then(res => res.json())
      .then(setPersons);
  };

  React.useEffect(() => {
    loadData();
  }, []);

  const addPerson = () => {
    fetch('../backend/index.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, phone })
    })
      .then(res => res.json())
      .then(() => {
        setName('');
        setEmail('');
        setPhone('');
        loadData();
      });
  };

  return (
    <div className="container mx-auto">
      <h1 className="text-2xl font-bold mb-4">Cadastro de Pessoas</h1>
      <div className="card shadow-lg p-4 mb-4 space-y-2">
        <div>
          <label className="label">Nome</label>
          <input className="input input-bordered w-full" value={name} onChange={e => setName(e.target.value)} />
        </div>
        <div>
          <label className="label">Email</label>
          <input className="input input-bordered w-full" value={email} onChange={e => setEmail(e.target.value)} />
        </div>
        <div>
          <label className="label">Telefone</label>
          <input className="input input-bordered w-full" value={phone} onChange={e => setPhone(e.target.value)} />
        </div>
        <button className="btn btn-primary" onClick={addPerson}>Cadastrar</button>
      </div>
      <table className="table w-full">
        <thead>
          <tr><th>Nome</th><th>Email</th><th>Telefone</th></tr>
        </thead>
        <tbody>
          {persons.map(p => (
            <tr key={p.id}>
              <td>{p.name}</td>
              <td>{p.email}</td>
              <td>{p.phone}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
