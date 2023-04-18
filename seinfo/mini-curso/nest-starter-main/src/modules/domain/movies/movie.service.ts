import { HttpException, HttpStatus, Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { ArrayContains } from "typeorm";
import { CreateMovieDto } from "./dto/create-movie.dto";
import { ArtistEntity } from "./entities/artist.entity";
import { GenreEntity } from "./entities/genre.entity";
import { MovieEntity } from "./entities/movie.module";

@Injectable()
export class MovieService{
    @InjectRepository(MovieEntity)
    private readonly movieRepository: Repository<MovieEntity>

    @InjectRepository(ArtistEntity)
    private readonly artistRepository: Repository<ArtistEntity>

    @InjectRepository(GenreEntity)
    private readonly genreRepository: Repository<GenreEntity>

    async createMovie(createMovieDto: CreateMovieDto){
        const director = this.artistRepository.findOneBy({
            id: createMovieDto.directorId,
        });
        if(!director)
            throw new HttpException('Ditector not found', HttpStatus.BAD_REQUEST);
        const cast = await this.artistRepository.findBy({
            id: ArrayContains(createMovieDto.castIds),
        });
        if(createMovieDto.castIds.length !== cast.length)
            throw new HttpException('Some actors not found', HttpStatus.BAD_REQUEST);
        const genres = await this.genreRepository.findBy({
            id: ArrayContains(createMovieDto.genresIds),
        });
        if(createMovieDto.genresIds.length !== genres.length)
            throw new HttpException('Some genres not found', HttpStatus.BAD_REQUEST);
        const newEntity = this.genreRepository.create({
            ...createMovieDto,
            director,
            moviesCast,
            genres,
        });
        return await this.movieRepository.save(newEntity);
    }


}