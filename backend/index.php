<?php
require __DIR__ . '/config.php';
header('Content-Type: application/json');

$method = $_SERVER['REQUEST_METHOD'];

if ($method === 'GET') {
    $stmt = $pdo->query("SELECT id, name, email, phone FROM persons ORDER BY id DESC");
    echo json_encode($stmt->fetchAll());
    exit;
}

if ($method === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    $stmt = $pdo->prepare("INSERT INTO persons (name, email, phone) VALUES (?, ?, ?)");
    $stmt->execute([
        $data['name'] ?? '',
        $data['email'] ?? '',
        $data['phone'] ?? ''
    ]);
    echo json_encode(['success' => true]);
    exit;
}

echo json_encode(['error' => 'Unsupported request']);
?>
