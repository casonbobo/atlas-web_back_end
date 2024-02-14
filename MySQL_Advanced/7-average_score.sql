-- Store the computed average score back into the users table
-- Compute the average score for the given user_id

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser @userId INT AS
BEGIN
    DECLARE avg_score FLOAT;

    SELECT avgScore = AVG(score)
    FROM corrections
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET averageScore = avg_score
    WHERE id = user_id;
END;
//
DELIMITER;
