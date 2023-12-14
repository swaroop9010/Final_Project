<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Divisions and Company</title>
</head>
<style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        h2 {
            margin-top: 20px; /* Adjust the margin as needed */
        }

        table {
            border-collapse: collapse;
            width: 80%; /* Adjust the width as needed */
            margin-top: 20px; /* Optional margin from the top */
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }
</style>
<body>
    <h2>Divisions and Company</h2>
    <table border="1">
        <tr>
            <th>Industry ID</th>
            <th>Division Name</th>
            <th>Company</th>
            <th>Headquarter</th>
            <th>Update</th>
            <th>Delete</th>
        </tr>
        % for item in data:
            <tr>
                <td>{{item['IndustryID']}}</td>
                <td>{{item['DivisionName']}}</td>
                <td>{{item['Company']}}</td>
                <td>{{item['Headquarter']}}</td>
                <td><a href="/update/{{item['IndustryID']}}">Update</a></td>
                <td><a href="/delete/{{item['IndustryID']}}">Delete</a></td>
            </tr>
        % end
    </table>
    <a href="/add">Add a new industry and division</a>
</body>
</html>
